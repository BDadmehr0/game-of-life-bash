#!/bin/bash

# Set the grid size
GRID_SIZE=10

# Initialize the grid
grid=()
for ((i = 0; i < GRID_SIZE; i++)); do
    for ((j = 0; j < GRID_SIZE; j++)); do
        grid[$i,$j]=0
    done
done

# Set the initial pattern
grid[2,1]=1
grid[2,2]=1
grid[2,3]=1

# Function to print the grid
print_grid() {
    for ((i = 0; i < GRID_SIZE; i++)); do
        for ((j = 0; j < GRID_SIZE; j++)); do
            if [[ ${grid[$i,$j]} -eq 1 ]]; then
                echo -n "X "
            else
                echo -n ". "
            fi
        done
        echo
    done
    echo
}

# Function to check the state of a cell
get_cell_state() {
    local row=$1
    local col=$2

    if [[ $row -lt 0 || $row -ge GRID_SIZE || $col -lt 0 || $col -ge GRID_SIZE ]]; then
        echo 0
    else
        echo ${grid[$row,$col]}
    fi
}

# Function to calculate the next generation of the grid
calculate_next_generation() {
    local new_grid=()

    for ((i = 0; i < GRID_SIZE; i++)); do
        for ((j = 0; j < GRID_SIZE; j++)); do
            local live_neighbors=0

            for ((dx = -1; dx <= 1; dx++)); do
                for ((dy = -1; dy <= 1; dy++)); do
                    if [[ $dx -eq 0 && $dy -eq 0 ]]; then
                        continue
                    fi

                    if [[ $(get_cell_state $((i + dx)) $((j + dy))) -eq 1 ]]; then
                        ((live_neighbors++))
                    fi
                done
            done

            if [[ ${grid[$i,$j]} -eq 1 && ($live_neighbors -lt 2 || $live_neighbors -gt 3) ]]; then
                new_grid[$i,$j]=0
            elif [[ ${grid[$i,$j]} -eq 0 && $live_neighbors -eq 3 ]]; then
                new_grid[$i,$j]=1
            else
                new_grid[$i,$j]=${grid[$i,$j]}
            fi
        done
    done

    grid=("${new_grid[@]}")
}

# Run the game
while true; do
    clear
    print_grid
    calculate_next_generation
    sleep 0.5
done
