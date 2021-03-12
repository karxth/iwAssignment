# Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.

paragraph = "there are three cat in the ash. they have one ear. we are in modern era. normed vector. demon has drone"
print(f'Demo Paragraph: \n{paragraph}\n')
word_list = list(set(paragraph.split()))
sorted_word_list = []
anagrams_list = []

for i in word_list:
    i = i.replace('.', '')
    sorted_word_list.append("".join(sorted(i)))
index_list = []

for i in sorted_word_list:
    if sorted_word_list.count(i) >= 2:
        x = [j for j in range(len(sorted_word_list)-1) if i == sorted_word_list[j]]
        index_list.append(x)

for i in index_list:
    for j in i:
        anagrams_list.append(word_list[j])

print(f'The anagrams in paragraph are\n{anagrams_list}')
