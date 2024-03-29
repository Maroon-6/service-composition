# Service Composition
## Part 1: Normal coding with synchronous API calls
Service Composition: Price sum of given order type for a specific user (by user_id)

Parameters: user_id (user/order microservice), order_tpye: PENDING | COMPLETE | CANCELLED (order microservice)

Test results:

> The price sum of PENDING orders for user_id: 3 is 149.95
> 
> The price sum of CANCELLED orders for user_id: 3 is 79.97
>  
> The price sum of COMPLETE orders for user_id: 3 is 24.99
>  
> The price sum of COMPLETE orders for user_id: 1 is 0


## Part 2: Asynchronous API calls with parallelism
Service Composition: Sum of lowest price of all ingredients from a given recipe name (by recipe_name)

Parameters: recipe_name (cocktail recipe microservice)

Process: get the the ingredients from given recipe_name, then parallel call inventories that match the given ingredients, fetch the lowest price, and finally return the total price
