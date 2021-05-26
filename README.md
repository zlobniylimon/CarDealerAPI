# Car Dealers API

## Used libraries
 - FastAPI
 - SQLalchemy
 - pydantic

**GET** /dealers/ - Read all dealers

---

**POST** /dealers/ - Create new dealer

JSON Schema:
```
{
  "name":
  {
    "description": "A name of car dealer company",
    "type": "string"
  },
  "required": "name"
}
```

---

**GET** /dealers/{dealer_id} - Read dealer 

---

**PUT** /dealers/{dealer_id} - Update dealer

JSON Schema:
```
{
  "name": 
  {
    "description": "A name of car dealer company",
    "type": "string"
  },
  "required": "name"
}
```

---

**DELETE** /dealers/{dealer_id} - Delete dealer

---

**GET** /cars/ - Read all cars

---

**POST** /cars/ - Create new car

JSON Schema:
```
{
  "model":
  {
    "description": "Model of car",
    "type": "string"
  },
  "price":
  {
    "description": "Price for car",
    "type": "number"
  },
  "dealer_id":
  {
    "description": "Dealer that sells this car",
    "type": "number"
  },
  "required": [ "model", "price", "dealer_id" ]
}
```

---

**GET** /cars/{car_id} - Read car

---

**PUT** /cars/{car_id} - Update car

JSON Schema:
```
{
  "model":
  {
    "description": "Model of car",
    "type": "string"
  },
  "price":
  {
    "description": "Price for car",
    "type": "number"
  },
  "dealer_id":
  {
    "description": "Dealer that sells this car",
    "type": "number"
  },
  "required": [ "model", "price", "dealer_id" ]
}
```

---

**DELETE** /cars/{car_id} - Delete car

---


