# SmartGen Project README

Welcome to **SmartGen**, an innovative platform designed to transform Instagram media into Amazon-ready product listings. This README details the technical concepts, architecture, and database structure behind the project to help developers and collaborators understand and contribute effectively.

---

## **Overview**

### **Objective**
SmartGen automates the process of:
1. Fetching Instagram media data for a user.
2. Processing the raw media into **Refined Products** by cleaning and eliminating duplicates.
3. Converting the **Refined Products** into **Amazon Listed Ready** items that are SEO-optimized and compliant with Amazon's guidelines.

---

## **Project Structure**

The project is divided into three primary schemas to ensure modularity and scalability:

1. **Media Schema**:
   - Stores raw Instagram media.
   - Links media to users and tracks engagement data.

2. **Refined Product Schema**:
   - Processes and organizes media into structured product data.
   - Removes duplicates and redundancies.

3. **Amazon Listed Ready Schema**:
   - Converts refined products into Amazon listings.
   - Ensures compliance with Amazon's SEO and formatting requirements.

---

## **Schemas**

### **1. Media Schema**
This schema stores raw media fetched from Instagram.

```javascript
const MediaSchema = new Schema({
  user_id: { type: Schema.Types.ObjectId, ref: "User", required: true },
  media_type: { type: String, enum: ["image", "video"], required: true },
  media_url: { type: String, required: true },
  caption: { type: String },
  hashtags: { type: [String] },
  engagement_metrics: {
    likes: { type: Number, default: 0 },
    comments: { type: Number, default: 0 },
  },
  created_at: { type: Date, default: Date.now },
  processed: { type: Boolean, default: false },
  refined_product: { type: Schema.Types.ObjectId, ref: "RefinedProduct" },
});
```

#### **Key Features**:
- **Raw Media Data**: Includes captions, hashtags, and engagement metrics.
- **User Association**: Links media to its owner via the `user_id`.
- **Processing State**: Tracks whether the media has been processed into a refined product.

---

### **2. Refined Product Schema**
This schema represents media after processing, ensuring it is cleaned and organized for Amazon listing preparation.

```javascript
const RefinedProductSchema = new Schema({
  user_id: { type: Schema.Types.ObjectId, ref: "User", required: true },
  media_files: { type: [Schema.Types.ObjectId], ref: "Media", required: true },
  product_name: { type: String, required: true },
  description: { type: String },
  keywords: { type: [String] },
  category: { type: String, required: true },
  processed_at: { type: Date, default: Date.now },
  amazon_ready_product: { type: Schema.Types.ObjectId, ref: "AmazonListedReady" },
});
```

#### **Key Features**:
- **Media Association**: Links multiple media files contributing to a single product.
- **Cleaned Data**: Stores product name, description, and relevant keywords after processing.
- **Bridge Schema**: Acts as an intermediary between Media and Amazon Listed Ready.

---

### **3. Amazon Listed Ready Schema**
This schema represents finalized product listings, optimized for Amazon compliance.

```javascript
const AmazonListedReadySchema = new Schema({
  user_id: { type: Schema.Types.ObjectId, ref: "User", required: true },
  refined_product: { type: Schema.Types.ObjectId, ref: "RefinedProduct", required: true },
  product_name: { type: String, required: true },
  description: { type: String, required: true },
  keywords: { type: [String], required: true },
  images: { type: [String], required: true },
  primary_image: { type: String, required: true },
  category: { type: String, required: true },
  dimensions: {
    height: { type: String, required: true },
    width: { type: String, required: true },
    depth: { type: String, required: true },
    weight: { type: String, required: true },
  },
  price: { type: String, required: true },
  stock_quantity: { type: Number, required: true },
  compliance_check: { type: Boolean, required: true },
  amazon_listing_id: { type: String, unique: true },
  listing_status: { type: String, required: true },
  brand: { type: String, required: true },
  bullet_points: { type: [String], required: true },
  asin: { type: String, unique: true },
  created_at: { type: Date, default: Date.now },
});
```

#### **Key Features**:
- **Amazon Compliance**: Tracks attributes like `primary_image`, `dimensions`, and `compliance_check`.
- **SEO Optimization**: Includes keywords and bullet points to enhance Amazon search visibility.
- **Unique Identifiers**: Fields like `asin` and `amazon_listing_id` ensure uniqueness across listings.

---

## **Workflow**

### **Step 1: Fetch Media**
- Media is fetched using the Instagram Graph API and stored in the `Media` collection.

### **Step 2: Process Media**
- Redundancies are removed, and media files are grouped into a single product in the `Refined Product` collection.

### **Step 3: Optimize for Amazon**
- Refined products are further processed for Amazon compliance, ensuring SEO optimization and formatting.

### **Step 4: Publish**
- The finalized products in the `Amazon Listed Ready` collection are published to Amazon using their Seller API.

---

## **Interrelationships**

1. **Media ↔ Refined Product**:
   - Each media entry links to one refined product via the `refined_product` field.
   - Refined products aggregate multiple media entries through the `media_files` array.

2. **Refined Product ↔ Amazon Listed Ready**:
   - Each refined product links to a single Amazon-ready product via the `amazon_ready_product` field.

---

## **Development Notes**

### **Technologies Used**
- **Backend**: Node.js with MongoDB for schema design and data storage.
- **API**: Instagram Graph API for media fetching.
- **Compliance**: Amazon Seller API for publishing listings.

### **Challenges Addressed**
- **Data Redundancy**: Solved by processing raw media into refined products.
- **Amazon Compliance**: Ensured by creating a dedicated schema with attributes like dimensions, stock, and SEO keywords.

---

## **Getting Started**

### **Installation**
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-repo/smartgen.git
cd smartgen
npm install
```

### **Environment Variables**
Create a `.env` file with the following:
```
MONGO_URI=<Your MongoDB Connection String>
INSTAGRAM_API_KEY=<Your Instagram API Key>
AMAZON_SELLER_API_KEY=<Your Amazon Seller API Key>
```

### **Run the Project**
Start the development server:
```bash
npm run dev
```

---

## **Future Enhancements**
- **Real-Time Token Refresh**: Automate refreshing of Instagram access tokens.
- **Advanced Insights**: Incorporate AI for better media-product matching.
- **Multi-Platform Support**: Extend support to platforms like Facebook and TikTok.

---

Feel free to contribute to the project and suggest new features! If you encounter any issues, open an issue in the repository.
