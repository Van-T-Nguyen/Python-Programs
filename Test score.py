#Van Nguyen
#4/10/2018
#Assignment 3

def main():
    scores = []
    grades = input("Please enter grades here: ")
    while grades != "":
        scores.append(float(grades))
        avg = float(sum(grades)) / len(scores)
        grades = input("Please enter grades here: ")
    print(max(scores), min(scores), avg)
main()