# file created by Majd Zayyad
# Takes words from an online folder and prints longest and shortest 5 words
import requests

url = "https://www.mit.edu/~ecprice/wordlist.10000"
req = requests.get(url, allow_redirects=True)

# text file
f = open("words.txt", "w")
f.write(req.content.decode('utf-8')) # decode into chars
f.close()

f = open("words.txt", "r")
str = f.read().splitlines() # read each line separately
shortest_five = []
longest_five = []
f.close()

for i in range(5):
    shortest = min(str, key=len) # take shortest word
    longest = max(str, key=len) # take longest word
    str.remove(shortest) # remove shortest
    str.remove(longest) # remove longest also so in the next iteration we get the second shortest and longest...
    shortest_five.append(shortest)
    longest_five.append(longest)

# print results
print("Shortest 5 words:")
print(shortest_five)
print("Longest 5 words:")
print(longest_five)




