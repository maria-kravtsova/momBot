# whatToWear
raspberry pi mom, it compares temperatures inside and the weather outside and tells you what to wear.

Every morning there is a struggle, what do I put on? This bot will analyze the temperature inside using DHT11
sensor and the weather outside using Weather Underground API. It then tweets what I should wear at different times.
Using the Twitter API the tweets will be sent at 5am, noon, and 5pm, in the following fashion:

momBot: Put a coat on, it's below 0 today.
momBot: Don't forget the umbrella! It's going to be 50 and raining all day.
momBot: Apartment is nice and toasty, it's t-shirt and shorts time.

To Do:
 - Setup Twitter API
 - Setup Weather Underground
 - Set the tweets
