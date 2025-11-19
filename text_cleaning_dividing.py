with open("scraped_data.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text[:1000])
  # Print the first 1000 characters to verify content 
# now cleaning the text , like removing extra spaces, new lines etc.
cleaned_text = ' '.join(text.split())
print(cleaned_text[:1000])
#
# cleaned_text = cleaned_text.replace('\n', ' ').replace('\r', ' ')
# # now dividing the text into chunks of 1000 characters each for processing
# chunk_size = 1000
