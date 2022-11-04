# Architectures-for-Big-Data-Assignment 1

![Çalışma Yüzeyi 6@100x-8](https://user-images.githubusercontent.com/51405534/199984982-c4ef9b49-938c-4c43-a5ec-9cc48eb13097.png) 


In general, the architecture transmits the data it receives from one database to another database under the desired conditions. While doing this transfer, it aims to impact as little as possible on the data base performance and therefore performs the operations on the Data Lake. The size of data held and needs can vary from client to client and case to case, so architectures should be as scalable as possible. The use of cache can increase the speed of data processing and make the architecture scalable.!


![Çalışma Yüzeyi 5@100x-8](https://user-images.githubusercontent.com/51405534/199985064-14c83e5b-4e13-414c-b605-c566ebf5542a.png)


After specifying the condition, the architecture first checks whether the data providing this condition is already kept in a cache in the cache list.

If there is a cache that holds the desired data

--A search is made in the data lake under the relevant conditions and LIMIT 1. This data is compared with the last data of the relevant cache. If the datas are the same, the data in the relevant cache is up-to-date and the data is returned, the relevant cache is brought to the beginning of the cache list. Thus, the searched data is found quickly.

--If the cache data is not up to date, the cache data is deleted, thrown to the end of the list and the data of other caches in the cache list are checked. 

If the data cannot be found in any cache, the relevant search is made in the Data Lake. The found data is written to the cache at the end of the cache list and brought to the beginning of the cache list. It is then returned.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

As the number of caches in the cache list increases, our probability of accessing data in different conditions will accelerate. The architecture has the scalability to determine the number of caches according to the needs of the customer.

In the desired situation, the customer can access the desired data by entering the UPLOAD_TS> $LAST_TS condition into the read_data function. In this sense, the architecture provides the requirements. In addition, it works as a reusable architecture by connecting to any other database architecture and creating different query functions in line with the needs.	

Finally, the entire architecture, together with the comment lines in the code, forms the technical basis for the design phase.
