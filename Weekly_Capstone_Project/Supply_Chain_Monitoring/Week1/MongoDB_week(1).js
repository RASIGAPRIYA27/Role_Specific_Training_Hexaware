use SupplyChainDB

// Create collection
db.createCollection("shipment_logs")

// Insert shipment documents
db.shipment_logs.insertMany([
  {
    shipment_id: "SHP101",
    order_id: 1,
    supplier_id: 4,
    product_name: "Laptop",
    quantity: 2,
    status: "Delivered",
    location: "Chennai",
    vehicle_no: "TN09AB1234",
    shipment_date: new Date("2026-06-01"),
    expected_delivery: new Date("2026-06-03")
  },
  {
    shipment_id: "SHP102",
    order_id: 2,
    supplier_id: 4,
    product_name: "Mouse",
    quantity: 5,
    status: "In Transit",
    location: "Bangalore",
    vehicle_no: "KA05XY7890",
    shipment_date: new Date("2026-06-02"),
    expected_delivery: new Date("2026-06-05")
  },
  {
    shipment_id: "SHP103",
    order_id: 3,
    supplier_id: 3,
    product_name: "Rice Bag",
    quantity: 3,
    status: "Delivered",
    location: "Hyderabad",
    vehicle_no: "TS10GH4567",
    shipment_date: new Date("2026-06-02"),
    expected_delivery: new Date("2026-06-04")
  },
  {
    shipment_id: "SHP104",
    order_id: 4,
    supplier_id: 3,
    product_name: "Cooking Oil",
    quantity: 10,
    status: "Pending",
    location: "Chennai",
    vehicle_no: "TN22PQ5678",
    shipment_date: new Date("2026-06-03"),
    expected_delivery: new Date("2026-06-06")
  },
  {
    shipment_id: "SHP105",
    order_id: 5,
    supplier_id: 4,
    product_name: "Monitor",
    quantity: 1,
    status: "In Transit",
    location: "Mumbai",
    vehicle_no: "MH20AA1122",
    shipment_date: new Date("2026-06-04"),
    expected_delivery: new Date("2026-06-07")
  },
  {
    shipment_id: "SHP106",
    order_id: 6,
    supplier_id: 4,
    product_name: "Keyboard",
    quantity: 2,
    status: "Delivered",
    location: "Coimbatore",
    vehicle_no: "TN38BB2211",
    shipment_date: new Date("2026-06-05"),
    expected_delivery: new Date("2026-06-07")
  },
  {
    shipment_id: "SHP107",
    order_id: 7,
    supplier_id: 5,
    product_name: "Notebook",
    quantity: 20,
    status: "Pending",
    location: "Salem",
    vehicle_no: "TN30CD6789",
    shipment_date: new Date("2026-06-05"),
    expected_delivery: new Date("2026-06-08")
  },
  {
    shipment_id: "SHP108",
    order_id: 8,
    supplier_id: 5,
    product_name: "Pen Pack",
    quantity: 15,
    status: "Delivered",
    location: "Madurai",
    vehicle_no: "TN58EF4455",
    shipment_date: new Date("2026-06-06"),
    expected_delivery: new Date("2026-06-08")
  },
  {
    shipment_id: "SHP109",
    order_id: 9,
    supplier_id: 3,
    product_name: "Sugar",
    quantity: 10,
    status: "In Transit",
    location: "Trichy",
    vehicle_no: "TN48JK3344",
    shipment_date: new Date("2026-06-06"),
    expected_delivery: new Date("2026-06-09")
  },
  {
    shipment_id: "SHP110",
    order_id: 10,
    supplier_id: 4,
    product_name: "Printer",
    quantity: 1,
    status: "Pending",
    location: "Erode",
    vehicle_no: "TN33MN9876",
    shipment_date: new Date("2026-06-07"),
    expected_delivery: new Date("2026-06-10")
  }
])

// Display all shipments
db.shipment_logs.find()

// Display delivered shipments
db.shipment_logs.find({ status: "Delivered" })

// Display pending shipments
db.shipment_logs.find({ status: "Pending" })

// Display shipments from Chennai
db.shipment_logs.find({ location: "Chennai" })

// Display only selected fields
db.shipment_logs.find(
  {},
  {
    shipment_id: 1,
    product_name: 1,
    status: 1,
    location: 1,
    _id: 0
  }
)

// Sort shipments by shipment date ascending
db.shipment_logs.find().sort({ shipment_date: 1 })

// Sort shipments by shipment date descending
db.shipment_logs.find().sort({ shipment_date: -1 })

// Display first 5 shipments
db.shipment_logs.find().limit(5)

// Update shipment status
db.shipment_logs.updateOne(
  { shipment_id: "SHP104" },
  {
    $set: {
      status: "In Transit"
    }
  }
)

// Update shipment location
db.shipment_logs.updateOne(
  { shipment_id: "SHP102" },
  {
    $set: {
      location: "Vellore"
    }
  }
)

// Delete one shipment
db.shipment_logs.deleteOne({
  shipment_id: "SHP110"
})

// Count shipments by status
db.shipment_logs.aggregate([
  {
    $group: {
      _id: "$status",
      total_shipments: {
        $sum: 1
      }
    }
  }
])

// Calculate total quantity of all shipments
db.shipment_logs.aggregate([
  {
    $group: {
      _id: null,
      TotalQuantity: {
        $sum: "$quantity"
      }
    }
  }
])

// Count shipments by location
db.shipment_logs.aggregate([
  {
    $group: {
      _id: "$location",
      Shipments: {
        $sum: 1
      }
    }
  },
  {
    $sort: {
      Shipments: -1
    }
  }
])

// Calculate average quantity
db.shipment_logs.aggregate([
  {
    $group: {
      _id: null,
      AverageQuantity: {
        $avg: "$quantity"
      }
    }
  }
])

// Find maximum quantity
db.shipment_logs.aggregate([
  {
    $group: {
      _id: null,
      MaximumQuantity: {
        $max: "$quantity"
      }
    }
  }
])

// Match only delivered shipments using aggregation
db.shipment_logs.aggregate([
  {
    $match: {
      status: "Delivered"
    }
  }
])

// Create index on shipment_id
db.shipment_logs.createIndex({
  shipment_id: 1
})

// Create index on status
db.shipment_logs.createIndex({
  status: 1
})

// Create index on shipment_date
db.shipment_logs.createIndex({
  shipment_date: 1
})

// Create compound index on status and shipment_date
db.shipment_logs.createIndex({
  status: 1,
  shipment_date: 1
})

// Display all indexes
db.shipment_logs.getIndexes()

// Count total documents
db.shipment_logs.countDocuments()

// Display distinct locations
db.shipment_logs.distinct("location")

// Display distinct shipment statuses
db.shipment_logs.distinct("status")

// Find shipments with expected delivery after 2026-06-05
db.shipment_logs.find({
  expected_delivery: {
    $gt: new Date("2026-06-05")
  }
})

// Find shipments with quantity greater than 5
db.shipment_logs.find({
  quantity: {
    $gt: 5
  }
})

// Find locations starting with C
db.shipment_logs.find({
  location: /^C/
})
