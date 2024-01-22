def towers_of_hanoi(n, source, target, auxiliary):
    """
    Move n disks from the source rod to the target rod using the auxiliary rod.
    
    Parameters:
    - n: Number of disks to move.
    - source: Source rod (initial position of the tower).
    - target: Target rod (final position of the tower).
    - auxiliary: Auxiliary rod (used for intermediate steps).
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n-1, auxiliary, target, source)

# Example usage:
number_of_disks = 3
source_rod = "A"
target_rod = "C"
auxiliary_rod = "B"

print(f"Towers of Hanoi with {number_of_disks} disks:")
towers_of_hanoi(number_of_disks, source_rod, target_rod, auxiliary_rod)
