use CustomerOrderDB

// Create collection
db.createCollection("customer_feedback")

// Insert feedback documents
db.customer_feedback.insertMany([
  {
    customer_id: 1,
    customer_name: "Arun",
    rating: 5,
    feedback: "Excellent delivery and packaging.",
    feedback_date: new Date("2026-06-03")
  },
  {
    customer_id: 2,
    customer_name: "Meena",
    rating: 2,
    feedback: "Delivery was delayed.",
    feedback_date: new Date("2026-06-04")
  },
  {
    customer_id: 3,
    customer_name: "Rahul",
    rating: 4,
    feedback: "Good quality product.",
    feedback_date: new Date("2026-06-05")
  },
  {
    customer_id: 4,
    customer_name: "Divya",
    rating: 3,
    feedback: "Packaging could be improved.",
    feedback_date: new Date("2026-06-05")
  },
  {
    customer_id: 5,
    customer_name: "Kiran",
    rating: 5,
    feedback: "Very satisfied.",
    feedback_date: new Date("2026-06-06")
  },
  {
    customer_id: 6,
    customer_name: "Sneha",
    rating: 4,
    feedback: "Delivery on time.",
    feedback_date: new Date("2026-06-06")
  },
  {
    customer_id: 7,
    customer_name: "John",
    rating: 1,
    feedback: "Received damaged item.",
    feedback_date: new Date("2026-06-07")
  },
  {
    customer_id: 8,
    customer_name: "Priya",
    rating: 5,
    feedback: "Excellent customer support.",
    feedback_date: new Date("2026-06-07")
  },
  {
    customer_id: 9,
    customer_name: "Akash",
    rating: 3,
    feedback: "Average experience.",
    feedback_date: new Date("2026-06-08")
  },
  {
    customer_id: 10,
    customer_name: "Ravi",
    rating: 4,
    feedback: "Fast delivery.",
    feedback_date: new Date("2026-06-08")
  }
])

// Display all feedback
db.customer_feedback.find()

// Display all feedback in pretty format
db.customer_feedback.find().pretty()

// Find feedback with rating 5
db.customer_feedback.find({ rating: 5 })

// Find feedback for customer_id 2
db.customer_feedback.find({ customer_id: 2 })

// Display selected fields
db.customer_feedback.find(
  {},
  {
    customer_name: 1,
    rating: 1,
    feedback: 1,
    _id: 0
  }
)

// Sort by rating descending
db.customer_feedback.find().sort({ rating: -1 })

// Display top 5 feedback records
db.customer_feedback.find().limit(5)

// Update rating for customer_id 2
db.customer_feedback.updateOne(
  { customer_id: 2 },
  { $set: { rating: 3 } }
)

// Delete customer feedback for customer_id 10
db.customer_feedback.deleteOne({ customer_id: 10 })

// Average rating
db.customer_feedback.aggregate([
  {
    $group: {
      _id: null,
      AverageRating: { $avg: "$rating" }
    }
  }
])

// Customer count by rating
db.customer_feedback.aggregate([
  {
    $group: {
      _id: "$rating",
      Customers: { $sum: 1 }
    }
  }
])

// Maximum rating
db.customer_feedback.aggregate([
  {
    $group: {
      _id: null,
      HighestRating: { $max: "$rating" }
    }
  }
])

// Create index on customer_id
db.customer_feedback.createIndex({
  customer_id: 1
})

// Create index on rating
db.customer_feedback.createIndex({
  rating: 1
})

// Create compound index on customer_id and rating
db.customer_feedback.createIndex({
  customer_id: 1,
  rating: 1
})

// Display all indexes
db.customer_feedback.getIndexes()

// Count all documents
db.customer_feedback.countDocuments()

// Display distinct ratings
db.customer_feedback.distinct("rating")
