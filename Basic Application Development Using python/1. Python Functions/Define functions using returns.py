#Define functions using returns
'''
এই প্রোগ্রামটির মূল কাজ হলো square নামক একটি ফাংশন ডিফাইন করা হয়েছে, যা একটি 
সংখ্যা নেয় এবং এর বর্গমূল হিসেবে তা রিটার্ন করে। তারপরে এই ফাংশনকে কল করে একটি 
সংখ্যা প্রদান করা হয়েছে এবং এর পরে আবার একবার একই সংখ্যা প্রদান করা হয়েছে। সংখ্যা 
5-এর জন্য, square(5) করলে হবে 5 এর বর্গ, অর্থাৎ 25।

তারপর, print(square(5) + square(5)) লাইনে এই দুইটি ফাংশনকে কল করে এবং তাদের 
বর্গমূল যোগ করে এবং এর পরে ফলাফলটি প্রিন্ট করা হয়েছে। তার ফলাফল হবে:
square(5) + square(5) =25+25=50
'''
def square(x):
    y=x*x
    return y
print(square(5) + square(5))

#Define functions without using returns
def welcame():
    print("Welcome to Computer Technology")
    print("Engineer Md Delowar Hossan")
welcame()
welcame() # এখানে যতগুলো ওয়েলকাম লিখবো কতগুলো প্রিন্ট করবে।
welcame()
welcame()
welcame()