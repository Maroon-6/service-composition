# Service Composition
#### Part 1: Normal coding with synchronous API calls
Service Compostion: Price sum of given order type for a specific user (by user_id)

Parameters: user_id (user/order microservice), order_tpye: PENDING | COMPLETE | CANCELLED (order microservice)

Test results:

> The price sum of PENDING orders for user_id: 3 is 149.95
> 
> The price sum of CANCELLED orders for user_id: 3 is 79.97
>  
> The price sum of COMPLETE orders for user_id: 3 is 24.99
>  
> The price sum of COMPLETE orders for user_id: 1 is 0
