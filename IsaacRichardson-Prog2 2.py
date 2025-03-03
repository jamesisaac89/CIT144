# Isaac Richardson

def main():

    total_scores = 0
    score_count = 0
    sentinel_value = 9999

    print("Calculate the average of a bunch of exam scores.")
    print("The scores can be intehers or floats.")
    print()


    while True:
        
        try:
            score = float(input("Enter a number. 9999 to quit: "))

            if score == sentinel_value:
                break

            if 0 <= score <= 100:
                total_scores += score
                score_count += 1
            else:
                print("Score is not in range. Please re-enter.")

        except ValueError:
            print("Score is not in range. Please re-enter.")

    if score_count > 0:
        average = total_scores / score_count
        print(f"\nThese {score_count} scores average as: {average:.1f}")
    else:
        print("No valid scores entered.")

if __name__ == "__main__":
    main()
