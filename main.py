"""
Main driver for the Numerical Methods project.
Runs both Question 7 (Interpolation) and Question 12 (Numerical Integration).
"""

import question7
import question12

if __name__ == "__main__":
    print("\n" + "="*60)
    print(" NUMERICAL METHODS PROJECT ".center(60, "="))
    print("="*60 + "\n")

    # Run Question 7
    print("\n>>> Running Question 7: Interpolation <<<\n")
    question7.main()

    # Pause so the user can see the plots before the next runs
    input("\nPress Enter to continue to Question 12...")

    # Run Question 12
    print("\n>>> Running Question 12: Numerical Integration <<<\n")
    question12.main()

    print("\n" + "="*60)
    print(" Project completed successfully! ".center(60, "="))
    print("="*60)