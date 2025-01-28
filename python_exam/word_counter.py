def count(x):
    counts = {}
    for element in x:
        counts[element] =counts.get(element,0)+1
    return counts

def display(x):
    print(x)

def main():
    user_input = input("Enter a list of elements separated by spaces: ")
    x = user_input.split() 
    counts = count(x)
    print(counts)

if __name__ == "__main__":
    main()