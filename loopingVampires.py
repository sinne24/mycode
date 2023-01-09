#!/usr/bin/python3
"""CHALLENGE 67 - Looping Vampires"""

def vampytimes_maker(line):
    """write lines into a file if the contain vampire"""
  
    line.rstrip("\n") # ensure the line does not have any trailing "\n" characters
    line = line + "\n"

    with open("vampytimes.txt", "a") as vamp_file:
        vamp_file.write(line + "\n")

    return line #end of function


def main():
        """runtime"""
        
        counter_dracula = 0

        with open("dracula.txt") as dracula:
            for line in dracula:
                if "vampire" in line.lower():
                    counter_dracula += 1 #add 1 to our counter

                    print(vampytimes_maker(line), end=" ")

        print("Total number of lines with the word vampire:", counter_dracula)


if __name__ == "__main__":
    main()
