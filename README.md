# Recommendation System API

A RESTful Recommendation System designed to provide personalized product recommendations based on user preferences and interactions.

---

## **Features**
- Add users and manage their preferences.
- Add products to a catalog with details.
- Log user-product interactions.
- Generate recommendations based on:
  - User interactions: Products users have engaged with.
  - Preferences: Products matching user preferences.

---

## **Requirements**
- Python 3.x
- Flask
- Requests

---

## **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/maggie-21/-MSCS-532-Project-Phase3.git  
   cd RecommendationSystem  

3. Install dependencies:
   ```bash
   pip install -r requirements.txt  

5. Start the server:
   ```bash 
   python3 App.py  

7. Try out the system:
   ```bash 
   python3 Main.py  

---

## **Endpoints**
### **Base URL**: http://127.0.0.1:5000

### **1. User Management**
- Add User: POST /add_user  
  Example payload: user_id and name.  

- Add User Preference: POST /add_user_preference  
  Example payload: user_id and preference.  

### **2. Product Management**
- Add Product: POST /add_product  
  Example payload: product_id, name, and price.  

### **3. User-Product Interactions**
- Log Interaction: POST /add_interaction  
  Example payload: user_id and product_id.  

### **4. Recommendations**
- Get Recommendations: GET /get_recommendations/<user_id>  

---

## **How to Run**
1. Run the Server:
   ```bash  
   python3 App.py  
    ```
   The server will start on http://127.0.0.1:5000.  

3. Test the System:
   ```bash
   python3 Main.py  
    ```
   This script interacts with the API to add data and retrieve recommendations.

---

## **Examples**
### **Adding a User**
```bash
curl -X POST http://127.0.0.1:5000/add_user -H "Content-Type: application/json" -d '{"user_id": 1, "name": "Alice"}'
```
### **Getting Recommendations**
```bash
curl http://127.0.0.1:5000/get_recommendations/1
```

---

## **Future Enhancements**
- Advanced recommendation algorithms, including collaborative filtering and content-based filtering.
- Deploy the API on a production platform like Heroku or AWS.
- Integrate a frontend for better user interaction.
- Add API documentation with Swagger.

