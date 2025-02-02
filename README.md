Initially, I used TF-IDF combined with Nearest Neighbor so that some context is stored by containing the 'repeatability' or frequence of the word and finding the similarities between the sentences. But the sentiment and space of the vector wasn't that big.

Then I moved with a sentence transformer that held was much more powerful, and held 512 nuerons instead of normally 256.

Here is the object used for POST method: #client side
```
{
    query: String | Null,
    similar_problems: True | False
}
```

Here is the object returned to the client: 
```
{
    returned_query: String | Null,
    method: String | Null, 
    answer: String | Null
}
```
