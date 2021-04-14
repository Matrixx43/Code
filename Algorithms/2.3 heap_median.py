import heapq

# Compute the median of an array of numbers in random order each time a new number is received. Then print the sum of the medians. Use two heaps for that.

def main():
    with open("pset_2_3.txt", "r") as fin:
        # Keep adding the medians
        acc_medians = 0
        # Declare two new heaps, to store the 50% lower and 50% higher elements, keeping this balance
        h_low = []
        h_high = []
        heapq.heapify(h_low)
        heapq.heapify(h_high)
        added_numbers = 0
        for line in fin.readlines():
            added_numbers += 1
            # Read a new number
            number = int(line)
            # Cehck in which heap it has to be added
            # If higher than lowest in top 50%, put it h_high
            if h_high:
                if number > h_high[0]:
                    heapq.heappush(h_high, number)
                else:
                    heapq.heappush(h_low, (-1) * number)
            else: # Very first element added
                heapq.heappush(h_high, number)
            # Adjust as necessary to make sure heaps are balanced. Make h_high the larger one if necessary
            if added_numbers % 2 == 0: # #Added numbers is even
                while (len(h_high) > len(h_low)):
                    # Move smallest element in h_high to h_low
                    heapq.heappush(h_low, (-1) * heapq.heappop(h_high))
                # opposite case cannot happen because, if there is an odd number of numbers, then h_high will always be larger
                # Calculate median as smallest among 2 median numbers
                acc_medians += (-1) * h_low[0]
                #print((-1) * h_low[0])
            else:
                # Make h_high always bigger
                if len(h_low) > len(h_high):
                    # Move biggest from h_low to h_high
                    heapq.heappush(h_high, (-1) * heapq.heappop(h_low))
                # Calculate median
                acc_medians += h_high[0]
                #print(h_high[0])
        print(acc_medians%10000)
            




main()