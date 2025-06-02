import React, { useRef } from 'react'
import { useState, useEffect, useCallback } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import axios from 'axios'
import { format } from 'date-fns'
import clsx from 'clsx'
import Confetti from 'react-confetti'
import { useWindowSize } from 'react-use'

interface Phrase {
  uuid: string
  phrase: string
  created: string
  last_updated: string
}

function Game() {
  const [phrase, setPhrase] = useState<Phrase | null>(null)
  const [input, setInput] = useState<string[]>([])
  const [errors, setErrors] = useState<boolean[]>([])
  const [startTime, setStartTime] = useState<Date | null>(null)
  const [elapsedTime, setElapsedTime] = useState(0)
  const [isGameComplete, setIsGameComplete] = useState(false); // New state for game completion
  const inputRefs = useRef<(HTMLInputElement | null)[]>([])
  const { width, height } = useWindowSize(); // Get window size for confetti

  const fetchRandomPhrase = useCallback(async () => {
    try {
      const response = await axios.get<Phrase>('http://127.0.0.1:8000/phrase/random')
      setPhrase(response.data)
      // Filter out spaces when creating input array
      const lettersOnly = response.data.phrase.replace(/\s+/g, '')
      setInput(new Array(lettersOnly.length).fill(''))
      setErrors(new Array(lettersOnly.length).fill(false))
      setStartTime(new Date())
      setIsGameComplete(false); // Reset game completion state
      // Reset refs array when new phrase is loaded
      inputRefs.current = new Array(lettersOnly.length).fill(null)
    } catch (error) {
      console.error('Error fetching phrase:', error)
    }
  }, [])

  useEffect(() => {
    fetchRandomPhrase()
  }, [fetchRandomPhrase])

  // Auto-focus the first input field when the phrase is loaded
  useEffect(() => {
      if (inputRefs.current.length > 0 && inputRefs.current[0]) {
          inputRefs.current[0].focus();
      }
  }, [phrase]); // Dependency on phrase ensures it focuses after a new phrase is fetched

  useEffect(() => {
    if (!startTime || isGameComplete) return // Stop timer if game is complete

    const timer = setInterval(() => {
      const now = new Date()
      const elapsed = (now.getTime() - startTime.getTime())
      setElapsedTime(elapsed)
    }, 100);

    return () => clearInterval(timer)
  }, [startTime, isGameComplete]); // Add isGameComplete to dependencies

  // Effect to handle Enter key press for Play Again
  useEffect(() => {
    const handleKeyPress = (event: KeyboardEvent) => {
      if (isGameComplete && event.key === 'Enter') {
        handlePlayAgain();
      }
    };

    document.addEventListener('keydown', handleKeyPress);

    return () => {
      document.removeEventListener('keydown', handleKeyPress);
    };
  }, [isGameComplete]); // Depend on isGameComplete to only add listener when needed

  const handleInputChange = (index: number, value: string) => {
    if (value.length > 1) return

    const newInput = [...input]
    newInput[index] = value.toUpperCase()

    // Get the sorted letters of the phrase, excluding spaces
    const phraseLettersSorted = phrase?.phrase.toUpperCase().replace(/\s+/g, '').split('').sort() || []

    const newErrors = [...errors]
    let isCurrentInputCorrect = false;

    if (value) {
        // Get all non-empty letters including the current input for checking the sequence up to this point
        const currentInputWithNewValue = [...newInput];
        const enteredLettersUpToIndexSorted = currentInputWithNewValue.filter(Boolean).sort();

        // Check if the sequence of entered letters up to and including this point is correct
        const isSequenceCorrectUpToIndex = enteredLettersUpToIndexSorted.every((letter, i) => letter === phraseLettersSorted[i]);

        // The current input is correct if the overall sequence up to this point is correct
        // This implicitly handles duplicates by checking the sorted sequence.
        isCurrentInputCorrect = isSequenceCorrectUpToIndex;

         newErrors[index] = !isCurrentInputCorrect;

    } else {
        // If the value is deleted, mark as not an error for now, re-evaluate based on overall state later if needed
         newErrors[index] = false;
    }

    setInput(newInput)
    setErrors(newErrors)

    // Check for game completion
    const updatedEnteredLetters = newInput.filter(Boolean);
    if (isCurrentInputCorrect && updatedEnteredLetters.length === phraseLettersSorted.length) {
        setIsGameComplete(true);
    }

    // If the current input is correct and it's not the last input field, focus the next empty input field
    if (isCurrentInputCorrect && value !== '' && index < input.length - 1) {
        // Find the next empty input field after the current one
        const nextEmptyIndex = newInput.findIndex((val, i) => val === '' && i > index);
        if(nextEmptyIndex !== -1) {
            inputRefs.current[nextEmptyIndex]?.focus();
        } else if (index < input.length - 1) { // If no empty fields after, just go to the next one if not the last
             inputRefs.current[index + 1]?.focus();
        }

    } else if (!value && isCurrentInputCorrect && index > 0) {
         // If deleting a correct letter and the sequence is still correct, focus the previous field
         inputRefs.current[index - 1]?.focus();
    }
  }

    const handleKeyDown = (index: number, e: React.KeyboardEvent<HTMLInputElement>) => {
        // If backspace is pressed and the current field is empty and it's not the first field, move focus to the previous field
        if (e.key === 'Backspace' && input[index] === '' && index > 0) {
            e.preventDefault(); // Prevent the default backspace behavior
            inputRefs.current[index - 1]?.focus();
        }
    };

    const handlePlayAgain = () => {
        setIsGameComplete(false); // Stop confetti and timer
        fetchRandomPhrase(); // Get a new phrase and reset game state
    };

  const formatTime = (milliseconds: number) => {
    const totalSeconds = Math.floor(milliseconds / 1000);
    const minutes = Math.floor(totalSeconds / 60);
    const remainingSeconds = totalSeconds % 60;
    const remainingMilliseconds = milliseconds % 1000;

    const formattedMinutes = String(minutes).padStart(2, '0');
    const formattedSeconds = String(remainingSeconds).padStart(2, '0');
    const formattedMilliseconds = String(remainingMilliseconds).padStart(3, '0');

    return `${formattedMinutes}:${formattedSeconds}:${formattedMilliseconds}`;
  }

  if (!phrase) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500"></div>
      </div>
    )
  }

  return (
    <div className="min-h-screen p-4 md:p-8 flex flex-col items-center">
      {isGameComplete && <Confetti width={width} height={height} numberOfPieces={500} recycle={false} tweenDuration={2000} confettiSource={{ x: 0, y: 0, w: width, h: 0 }} />}
      <div className="max-w-2xl w-full space-y-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-primary-600 mb-4">AlphaRush</h1>
          {/* Instructions */}
          <p className="text-xl text-gray-700 mb-4">Enter the letters in alphabetical order.</p>
          <p className="text-2xl font-semibold mb-8">{phrase.phrase}</p>
        </div>

        <div className="flex flex-wrap justify-center gap-2">
          {input.map((letter, index) => (
            <input
              key={index}
              ref={el => inputRefs.current[index] = el}
              type="text"
              maxLength={1}
              value={letter}
              onChange={(e) => handleInputChange(index, e.target.value)}
              onKeyDown={(e) => handleKeyDown(index, e)} // Add onKeyDown handler
              className={clsx('input-letter', {
                'error': errors[index],
                'correct': letter && !errors[index] // Correct if there's a letter and it's not an error
              })}
              disabled={isGameComplete} // Disable input fields when game is complete
            />
          ))}
        </div>

        <div className="text-center mt-8 fixed bottom-4 left-0 right-0 z-10">
          <div className="text-3xl font-mono font-bold text-primary-600">
            {formatTime(elapsedTime)}
          </div>
           {/* Play Again Button */}
           {isGameComplete && (
            <button
              onClick={handlePlayAgain}
              className="mt-4 px-6 py-3 bg-primary-500 text-white font-bold rounded-md hover:bg-primary-600 focus:outline-none"
            >
              Play Again
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Game />} />
      </Routes>
    </Router>
  )
}

export default App
