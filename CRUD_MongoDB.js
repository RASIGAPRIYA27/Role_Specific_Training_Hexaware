// Switch to database
use retail_db;

// Create collection
db.createCollection('customer');

// Insert single document
db.customer.insertOne({
    customer_id: 1,
    name: 'Priya',
    city: 'Bangalore',
    phone: '9876543210',
    membership: "Gold"
});

// Insert multiple documents
db.customer.insertMany([
    {
        customer_id: 2,
        name: 'Rasiga',
        city: 'Chennai',
        phone: '7676543110',
        membership: "Silver"
    },
    {
        customer_id: 3,
        name: 'Gigi',
        city: 'Bangalore',
        phone: null,
        membership: "Bronze"
    },
    {
        customer_id: 4,
        name: 'Harish',
        city: 'Hyderabad',
        phone: '9853443210',
        membership: "Gold"
    }
]);

// Find greater than 2
db.customer.find({
    customer_id: { $gt: 2 }
});

// Find less than or equal to 3
db.customer.find({
    customer_id: { $lte: 3 }
});

// Find all 
db.customer.find();

// Find field
db.customer.find({
    city: 'Chennai'
});

// Find IN
db.customer.find({
    city: { $in: ['Chennai', 'Bangalore'] }
});

// Find AND
db.customer.find({
    city: 'Bangalore',
    membership: 'Gold'
});

// Find OR
db.customer.find({
    $or: [
        { city: 'Bangalore' },
        { membership: 'Gold' }
    ]
});

// Find only specified fields
db.customer.find({},
    { name: 1, city: 1, _id: 0 }
);

// Sort in ascending
db.customer.find().sort({ customer_id: 1 });

// Sort in descending
db.customer.find().sort({ customer_id: -1 });

// Limit results 
db.customer.find().limit(3);