def run ():
    result = {i: round(i**0.5, 3) for i in range (1, 1001)}
    print (result)

if __name__ == "__main__":
    run ()