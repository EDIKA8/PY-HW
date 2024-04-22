
                                 #Homework
                              
def merge_lists(list1, list2): #1
    
    set1 = set(list1)
    set2 = set(list2)
    
    merged_set = set1.union(set2)
    
    merged_list = sorted(merged_set)
    
    return merged_list

list1 = [1, 2, 3]
list2 = [3, 4, 5]
result = merge_lists(list1, list2)
print(result)



input_list = [1, 2, 3, 4, 5] #2

squared_list = [x ** 2 for x in input_list]

print(squared_list)


def filter_odd_numbers(numbers): #3
    return [num for num in numbers if num % 2 != 0]

numbers = [1, 2, 3, 4, 5]
odd_numbers = filter_odd_numbers(numbers)
print(odd_numbers)  



def find_common_elements(list1, list2): #4
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = find_common_elements(list1, list2)
print(common_elements)  



def remove_duplicates_preserve_order(lst): #5
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

lst = [1, 2, 3, 2, 4, 1]
result = remove_duplicates_preserve_order(lst)
print(result)



def merge_dictionaries(dict1, dict2): #6
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result = merge_dictionaries(dict1, dict2)
print(result)



input_dict = {'a': 1, 'b': 2, 'c': 3} #7
squared_dict = {key: value ** 2 for key, value in input_dict.items()}
print(squared_dict)



def extract_keys_as_list(input_dict): #8
    return list(input_dict.keys())

input_dict = {'a': 1, 'b': 2, 'c': 3}
keys_list = extract_keys_as_list(input_dict)
print(keys_list) 



def word_frequency_counter(text): #9
    words = text.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

text = "hello world hello"
freq_dict = word_frequency_counter(text)
print(freq_dict)  



def filter_dict_by_value(input_dict, value): #10
    return {key: val for key, val in input_dict.items() if val == value}

input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
filtered_dict = filter_dict_by_value(input_dict, 1)
print(filtered_dict) 



def factorial(n): #11
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
fact = factorial(number)
print(f"The factorial of {number} is {fact}") 



def is_palindrome(s): #12
    s = s.lower()
    return s == s[::-1]

string = "radar"
print(is_palindrome(string))



def is_anagram(str1, str2): #13
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)

word1 = "listen"
word2 = "silent"
print(is_anagram(word1, word2)) 



import re #14

def reverse_sentence(sentence):
    words = re.findall(r"[\w']+|[.,!?;]", sentence)
    reversed_words = words[::-1]
    return ''.join(reversed_words)

sentence = "Hello, world! How are you?"
print(reverse_sentence(sentence)) 



class TodoList: #15
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in the list.")

    def view_list(self):
        return self.items

my_list = TodoList()
my_list.add_item("Task 1")
my_list.add_item("Task 2")
my_list.add_item("Task 3")
print(my_list.view_list()) 
my_list.remove_item("Task 2")
print(my_list.view_list())  



def lists_to_dictionary(keys, values): #16
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result_dict = lists_to_dictionary(keys, values)
print(result_dict)



def is_key_present(dictionary, key): #17
    return key in dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(is_key_present(my_dict, 'b')) 



def aggregate_values(dictionary): #18
    result_dict = {}
    for key, values in dictionary.items():
        result_dict[key] = sum(values)
    return result_dict

my_dict = {'a': [1, 2, 3], 'b': [4, 5]}
result = aggregate_values(my_dict)
print(result) 



def split_list_by_value(lst, value): #19
    return [x for x in lst if x < value], [x for x in lst if x >= value]

my_list = [3, 1, 5, 2, 4, 6]
lower, greater_equal = split_list_by_value(my_list, 4)
print("Elements less than 4:", lower)
print("Elements greater than or equal to 4:", greater_equal)  



def count_common_elements(list1, list2): #20
    set1 = set(list1)
    set2 = set(list2)
    return len(set1 & set2)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
count = count_common_elements(list1, list2)
print(count) 
