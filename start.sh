#!/bin/bash
# Start milvus-server in the background
echo "Staring Milvus..."

milvus-server &

sleep 30

echo "Staring App..."

#!/bin/bash

# Command to run
command="python3 app.py"

# Maximum number of retries
max_retries=5

# Initial retry count
retry_count=0

# Delay between retries in seconds
delay=5

# Loop until the command succeeds or we reach the maximum number of retries
while true; do
    # Execute the command
    $command

    # Capture the exit status
    status=$?

    # Check if the command succeeded
    if [ $status -eq 0 ]; then
        echo "Command succeeded."
        break
    else
        # Increment the retry count
        ((retry_count++))

        # Check if we've reached the maximum number of retries
        if [ $retry_count -le $max_retries ]; then
            echo "Command failed with status $status. Attempting retry $retry_count of $max_retries."
            sleep $delay
        else
            echo "Command failed after $max_retries retries. Giving up."
            break
        fi
    fi
done
