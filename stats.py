import matplotlib.pyplot as plt
import csv
def read_hours(filename):
    hours = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hr = row['Exercise'].strip()
            if hr != '':
                try:
                    hours.append(float(hr))
                except ValueError:
                    continue
    return hours
def make_histogram(data):
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.title("Histogram of Exercist Hours")
    plt.xlabel("Hours of Exercise")
    plt.ylabel("Frequency")
    plt.show()
def average(ls):
    if len(ls) == 0:
        return 0
    return sum(ls)/len(ls)
def prop_above(ls):
    avg = average(ls)
    count_above = sum(1 for x in ls if x > avg)
    return count_above/len(ls)
def median(ls):
    sorted_ls = sorted(ls)
    n = len(sorted_ls)
    mid = n//2
    if n % 2 == 0:
        return(sorted_ls[mid - 1] + sorted_ls[mid])/2
    else:
        return sorted_ls[mid]
def main():
    filename = "StudentExercise.csv"
    hours = read_hours(filename)
    print(f"Data read successfully: {hours}")
    make_histogram(hours)
    avg = average(hours)
    prop = prop_above(hours)
    med = median(hours)
    print(f"Average hours of exercise: {avg:.2f}")
    print(f"Proportion of students above average: {prop:.2f}")
    print(f"Median hours of exercise: {med:.2f}")
if __name__ == "__main__":
    main()
