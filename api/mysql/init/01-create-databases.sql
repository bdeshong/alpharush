-- Create databases for different environments
CREATE DATABASE IF NOT EXISTS alphasort_dev;
CREATE DATABASE IF NOT EXISTS alphasort_staging;
CREATE DATABASE IF NOT EXISTS alphasort;

-- Grant privileges to the alphasort user
GRANT ALL PRIVILEGES ON alphasort_dev.* TO 'alphasort'@'%';
GRANT ALL PRIVILEGES ON alphasort_staging.* TO 'alphasort'@'%';
GRANT ALL PRIVILEGES ON alphasort.* TO 'alphasort'@'%';
FLUSH PRIVILEGES;
