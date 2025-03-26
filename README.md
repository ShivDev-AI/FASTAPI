Test the API:

GET /products - Get a list of all products.

GET /products/{product_id} - Get details for a specific product.

POST /products - Add a new product.

PUT /products/{product_id} - Update an existing product.

DELETE /products/{product_id} - Delete a product.

User Registration and Login:

POST /register - Register a new user (username and password).

POST /token - Login a user and get an access token.

Explanation:
/register: This route allows new users to register by providing a username and password. The password is stored in-memory in users_db.

/token: This route authenticates users by checking the username and password. If valid, it returns an access token (a simple token in this case).

/products: Lists all products available.

/products/{product_id}: Fetches details of a specific product by its product_id.

/products (POST): Adds a new product to the "database" (in-memory dictionary).

/products/{product_id} (PUT): Updates the details of a specific product.

/products/{product_id} (DELETE): Deletes a product from the database.