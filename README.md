# momBot

# weather conditions
raspberry pi mom, it compares temperatures inside and the weather outside and tells you what to wear.

Every morning there is a struggle, what do I put on? This bot will analyze the temperature inside using DHT11
sensor and the weather outside using Open Weather Map API. It then tweets what I should wear at different times.
Using the Twitter API the tweets will be sent at 5am, noon, and 5pm, in the following fashion:

momBot: Put a coat on, it's below 0 today.
momBot: Don't forget the umbrella! It's going to be 50 and raining all day.
momBot: Apartment is nice and toasty, it's t-shirt and shorts time.

# alarm clock
Unless the button is pushed on the raspberry pi by 6 am, mom bot will send shame tweets

momBot: Mariia is still asleep. Let's all start calling her.
momBot: This is what you get for staying late last night again.
