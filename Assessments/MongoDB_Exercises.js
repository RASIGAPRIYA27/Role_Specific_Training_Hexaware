use food_delivery_assessment_db

//create collection
db.createCollection('restaurants')

//insert data
db.restaurants.insertMany([
{
restaurant_id: 1,
name: "Spice Hub",
city: "Hyderabad",
cuisine: "Indian",
rating: 4.5,
avg_order_value: 450,
delivery_available: true,
tags: ["biryani", "north indian", "family"],
contact: {
phone: "9876543210",
email: "spicehub@mail.com"
}
},
{
restaurant_id: 2,
name: "Pizza Corner",
city: "Bangalore",

cuisine: "Italian",
rating: 4.2,
avg_order_value: 600,
delivery_available: true,
tags: ["pizza", "fast food", "cheese"],
contact: {
phone: "9876543211",
email: "pizza@mail.com"
}
},
{
restaurant_id: 3,
name: "Green Bowl",
city: "Chennai",
cuisine: "Healthy",
rating: 4.7,
avg_order_value: 350,
delivery_available: false,
tags: ["salad", "vegan", "healthy"],
contact: {
phone: null,
email: "greenbowl@mail.com"
}
},
{
restaurant_id: 4,
name: "Burger Street",
city: "Hyderabad",
cuisine: "Fast Food",
rating: 3.9,
avg_order_value: 300,
delivery_available: true,
tags: ["burger", "fries", "fast food"],
contact: {
phone: "9876543213",
email: null
}
},
{
restaurant_id: 5,
name: "Royal Tandoor",
city: "Delhi",
cuisine: "Indian",
rating: 4.8,

avg_order_value: 800,
delivery_available: true,
tags: ["tandoor", "north indian", "premium"],
contact: {
phone: "9876543214",
email: "royal@mail.com"
}
},
{
restaurant_id: 6,
name: "Tea Tales",
city: "Pune",
cuisine: "Cafe",
rating: 4.1,
avg_order_value: 200,
delivery_available: false,
tags: ["tea", "snacks", "cafe"],
contact: {
phone: "9876543215",
email: "tea@mail.com"
}
},
{
restaurant_id: 7,
name: "Ocean Grill",
city: "Mumbai",
cuisine: "Seafood",
rating: 4.6,
avg_order_value: 900,
delivery_available: true,
tags: ["fish", "grill", "premium"],
contact: {
phone: "9876543216",
email: "ocean@mail.com"
}
},
{
restaurant_id: 8,
name: "Dosa Point",
city: "Chennai",
cuisine: "South Indian",
rating: 4.3,
avg_order_value: 250,
delivery_available: true,

tags: ["dosa", "idli", "breakfast"],
contact: {
phone: null,
email: null
}
}
])

// 1. Display all
db.restaurants.find()

// 2. Display only specified
db.restaurants.find(
  {},{name:1,city: 1,cuisine:1,_id:0}
)

// 3. Find all from Hyderabad
db.restaurants.find({city:'Hyderabad'})

// 4. Find all Indian cuisine 
db.restaurants.find({cuisine:'Indian'})

// 5. Find delivery is available
db.restaurants.find({delivery_available:true})

// 6. Find rating greater than 4.5
db.restaurants.find({rating:{$gt:4.5}})

// 7. Find avg_order_value is less than ₹400
db.restaurants.find({avg_order_value:{$lte:400}})

// 8. Find rating between 4.0 and 4.7
db.restaurants.find({rating:{$gt:4.0,$lte:4.7}})

// 9. Find  avg_order_value >= ₹600
db.restaurants.find({avg_order_value:{$gt:600}})

// 10. Find all Hyderabad with delivery available
db.restaurants.find(
  {city:'Hyderabad',
  delivery_available:true}
)

// 11. Find either from Chennai OR cuisine is Indian
db.restaurants.find(
{ $or:[ {city:'Chennai'},
        {cuisine:'Indian'}]})

// 12. Find where delivery is NOT available
db.restaurants.find({delivery_available:false})

// 13. Find restaurants from: Hyderabad, Delhi, Mumbai
db.restaurants.find(
{city:{ $in:['Hyderabad','Delhi','Mumbai']}}
)

// 14. Find whose cuisine is Indian, Italian, or Cafe
db.restaurants.find(
{cuisine:{ $in:['Indian','Italian','Cafe']}})

// 15. Find restaurants NOT located in Hyderabad, Bangalore
db.restaurants.find({city:{$nin:['Hyderabad','Bangalore']}})

// 16. Find name starts with 'P'
db.restaurants.find({ name: { $regex: /^P/ } });

// 17. Find name contains 'Point'
db.restaurants.find({ name: { $regex: /Point/ } })

// 18. Find cuisine contains 'Food'
db.restaurants.find({ cuisine: { $regex: /Food/ } })

// 19. Find contact phone is null
db.restaurants.find({'contact.phone': null })

// 20. Find restaurants where contact email is null
db.restaurants.find({'contact.email': null })

// 21. find Either phone or email is null.
db.restaurants.find({$or:[ {'contact.email': null },{'contact.phone': null }]})

// 22. Find restaurant having tag premium.
db.restaurants.find({tags:'premium'})

// 23. find restaurants having tag fast food.
db.restaurants.find({tags:'fast food'})

// 24. Find restaurants having both tags. North Indian and premium.
db.restaurants.find({tags:{$all:['north indian','premium']}})


// 25. sort rating in descending.
db.restaurants.find().sort({restaurant_id:-1})

// 26. display top three highest rated restaurants.
db.restaurants.find().sort({restaurant_id:-1}).limit(3)


// 27. Start restaurant by average order value ascending.
db.restaurants.find().sort({avg_order_value:1})


// 28. display top two expensive restaurant by average order value.
db.restaurants.find().sort({avg_order_value:-1}).limit(2)

// 29. update one document.
db.restaurants.updateOne({name:'Burger Street'},{$set:{rating:4.0}})

// 30. Update one document.
db.restaurants.updateOne({name:'Tea Tales'},{$set:{delivery_available: true}})

// 31. Update many document.
db.restaurants.updateMany({},{$set:{active:true}})

// 32. add a new tag.
db.restaurants.updateOne({name:'Spice Hub'},{$push:{tags:"popular"}})

// 33. remove the field from all document.
db.restaurants.updateMany(
    {},
    { $unset: { active: "" } }
);

// 34. Delete from one document.
db.restaurants.deleteOne({restaurant_id:6})

// 35. Delete from many document.
db.restaurants.deleteMany({rating:{$lte:4.0}})

// 36. Count total documents.
db.restaurants.countDocuments()

// 37. Count the document with specific field.
db.restaurants.countDocuments({delivery_available:true})

// 38. Display distinct field.
db.restaurants.distinct('city')

// 39. Display distinct field.
db.restaurants.distinct('cuisine')

// 40. Count by city.
db.restaurants.aggregate([
    { $group: { _id: "$city", count: { $sum: 1 } } }
]);

// 41. count by cuisine.
db.restaurants.aggregate([
    { $group: { _id: "$cuisine", count: { $sum: 1 } } }
]);

// 42. find average rating by cuisine
db.restaurants.aggregate([
    { $group: { _id: "$cuisine", avg_rating: { $avg: "$rating" } } }
]);

// 43. Find average order value by city.
db.restaurants.aggregate([
    { $group: { _id: "$city", avg_order_value: { $avg: "$avg_order_value" } } }
]);

// 44. find highest average order value by cuisine.
db.restaurants.aggregate([
    { $group: { _id: "$cuisine", avg_order_value: { $avg: "$avg_order_value" } } },
    { $sort: { avg_order_value: -1 } },
    { $limit: 1 }
]);

// 45. show cuisines having more than one restaurant.
db.restaurants.aggregate([
    { $group: { _id: "$cuisine", count: { $sum: 1 } } },
    { $match: { count: { $gt: 1 } } }
]);



