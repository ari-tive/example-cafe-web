import os
import re

base_dir = r"c:\Users\Administrator\Desktop\WEB BUSSINESS\websites\cafeweb-example\cafevelvet"

# 1. index.html
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('© 2023 Cafe Velvet. All Rights Reserved.', '© 2024 Cafe Velvet. All ingredients are locally sourced and organic.')
content = content.replace('Step into a world of tranquility at Cafe Velvet. Our space is mindfully designed as a lush retreat, surrounded by vibrant ferns, climbing ivy, and verdant greenery. Whether you seek a moment of solitude with a book or a nourishing catch-up with friends, our organic environment provides the perfect backdrop for rejuvenation.', 'Relax in a calm space filled with greenery, warm coffee, and healthy flavors. Surrounded by plants and natural light, Cafe Velvet is the perfect place to unwind, meet friends, or enjoy a quiet moment to yourself.')
content = content.replace('A Peaceful Oasis', 'Your calm escape from the city~!')

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(content)

# 2. contacts.html
with open(os.path.join(base_dir, 'contacts.html'), 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('© 2024 Cafe Velvet. All rights reserved.', '© 2024 Cafe Velvet. All ingredients are locally sourced and organic.')

with open(os.path.join(base_dir, 'contacts.html'), 'w', encoding='utf-8') as f:
    f.write(content)

# 3. menu.html
with open(os.path.join(base_dir, 'menu.html'), 'r', encoding='utf-8') as f:
    content = f.read()

# Replace prices
def replace_price(match):
    price_usd = float(match.group(1))
    price_inr = int(price_usd * 80)
    return f"₹{price_inr}"
content = re.sub(r'\$(\d+\.\d{2})', replace_price, content)

content = content.replace("A botanical oasis of hand-crafted flavors &amp; natural ingredients", "Full of hand-crafted flavors &amp; natural ingredients")
content = content.replace("A botanical oasis of hand-crafted flavors & natural ingredients", "Full of hand-crafted flavors & natural ingredients")

# Remove rewards card
start_idx = content.find('<div class="mt-20 p-8 rounded-3xl bg-sage-100')
if start_idx != -1:
    end_idx = content.find('</div>\n</div>\n</main>')
    if end_idx != -1:
        content = content[:start_idx] + content[end_idx:]

with open(os.path.join(base_dir, 'menu.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated text contents.")
