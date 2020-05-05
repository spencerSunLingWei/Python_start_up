import random

def deck(categories, num_of_cards_per_cat):
    """
    (list, int) -> list
    Given a list of strings representation as category names and an integer
    indicating the number of cards in one category,
    return a deck of cards as a list. For example, with ["spades", "hearts"], 2,
    return a list of list: [["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]],
    where 1 and 2 are the index of the cards.
    >> deck(["spades", "hearts"], 2)
    [["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]]
    >> deck(["spades", "hearts"], -5)
    []
    """
    result=[]
    if num_of_cards_per_cat > 0:
        for i in categories:
            number=0
            while number < num_of_cards_per_cat:
                number+=1
                result.append([i,number])
    return result


def random_shuffle(lst):
    """
    (list) -> list
    Receives a deck of cards and returns a randomly ordered
    list containing all of the same elements.
    The returned list should preserve the order of the categories. See below
    console outputs as an example, where "s" and "d" stay in the same order as
    the input and only the numbers are shuffled.
    >> random_shuffle([["s",1],["s",2],["s",3],["d",1],["d",2],["d",3]])
    [["s",3],["s",1],["s",2],["d",2],["d",1],["d",3]]
    """
    a=0
    category=lst[0][0]
    for i in lst:
        if category in i:
            a+=1
        else:
            break
        
    
    result=[]
    b=0
    while b+a<=len(lst):
        result+=random.sample(lst[b:b+a],a)
        b+=a
    
    return result

      



def reverse(lst):
    """
    (list) -> list
    Receives a list and returns a reverse ordered list containing all of the same elements.
    >> reverse([["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]])
    [["hearts", 2], ["hearts", 1], ["spades", 2],["spades",1]]
    """
    return lst[::-1]



