def top_n(items, n):
    """ Return the top n item in an Array in descending order

    Args:
        items(array): list or aaray like object
        n(int): number of items to return

    Return:
        array: top n items, in descending order.
    
    Egs:
        >>> top_n([8,9,3,6,2,4,5,7], 5)
            output = ([9,8,7])
            
    """
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items) -1, -i):

            if items[j] > items[j+1]: #if this item is bigger than next item
                items[j], items[j+1] = items[j+1], items[j] #swap the two!

    #get last two items
    top_n = items[-n:]

    # Return in desc order
    return top_n[: : -1]
            

    
