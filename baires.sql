-- Write a query to fetch the full name of the customers (The last name should be in upper case)
-- and the amount spent by them on orders. The result should be sorted by the amount spent in descending order and then in alphabetical order of the customer name.

-- orders table:
-- +-------------+--------+--------+
-- | Field | Type  | Desc |
-- order_id | int | order id |
-- order_product | string | product name |
-- ordered_by | int | customer id |
-- price | int | price of the product |

-- Customers table:
-- +-------------+--------+--------+
-- | Field | Type  | Desc |
-- customer_id | int | customer id |
-- first_name | string | first name |
-- last_name | string | last name |

-- Output format:
-- +-------------+--------+----------------+
-- | Field | Type  | Desc |
-- customer_name | string | full name of the customer |
-- total_amt_spent | int | total amount spent by the customer |

-- Solution in mysql

select concat(first_name, ' ', upper(last_name)) as customer_name, sum(price) as total_amt_spent
from customers

join orders
on customers.customer_id = orders.ordered_by
group by ordered_by
order by total_amt_spent desc, customer_name;


