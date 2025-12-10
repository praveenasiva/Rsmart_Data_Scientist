


# Set up the Chrome browser
genral = webdriver.Chrome()  # Make sure chromedriver is in your PATH

# Open Ajio's Fastrack watches page
driver.get("https://www.ajio.com/search/?text=fastrack%20watches")
time.sleep(3)  # Wait for page to load

# Lists to store our data
watch_names = []
prices = []
discounts = []

# Find all watch products on the page
# (This finds each product box - you can check this by inspecting the page)
products = driver.find_elements(By.CLASS_NAME, "item")  # Simple class name selector

print(f"Found {len(products)} watches")

for product in products:
    try:
        # Get watch name
        name = product.find_element(By.CLASS_NAME, "nameCls").text
        
        # Get price (using class name)
        price = product.find_element(By.CLASS_NAME, "price").text.replace('₹', '')
        
        # Try to get discount (not all products have discounts)
        try:
            discount = product.find_element(By.CLASS_NAME, "discount").text
        except:
            discount = "No discount"
        
        # Add to our lists
        watch_names.append(name)
        prices.append(price)
        discounts.append(discount)
        
    except Exception as e:
        print(f"Couldn't get one product: {e}")
        continue

# Close the browser
driver.quit()

# Create a DataFrame and save to Excel
if len(watch_names) > 0:
    data = pd.DataFrame({
        'Watch Name': watch_names,
        'Price': prices,
        'Discount': discounts
    })
    
    data.to_excel("fastrack_watches.xlsx", index=False)
    print("Successfully saved data to fastrack_watches.xlsx")
else:
    print("No watches found. Please check the website or selectors.")


