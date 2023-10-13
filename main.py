sorted_list = [1,3,5,7,9,11,13,15,17,19]

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def user_interface():
    print(f"the list of number{sorted_list}")
    while True:
        target = int(input("Enter a number to search for (or 0 to exit): "))
        if target == 0:
            break
        result = binary_search(sorted_list, target)
        if result != -1:
            print(f"{target} fount at index {result}")
        else:
            print(f"{target} not found in the list") 
       
            
if __name__ == "__main__":
    user_interface()