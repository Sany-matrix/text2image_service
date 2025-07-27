<<<<<<< HEAD
# 🖼️ Text-to-Image Generator with FastAPI

This project is a simple **text-to-image** generation service built with **FastAPI** and integrated with **OpenAI's image API (DALL·E)**.

## 🚀 Features

- Accepts a text prompt from the user
- Sends it to OpenAI to generate an image
- Returns the image URL in the response
- Includes unit tests using `pytest` and `monkeypatch`
- Containerized using Docker for deployment

---

## 📦 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text2image_service.git
   cd text2image_service


Limitations

This project is fully functional and all core features were implemented and tested successfully.
However, due to external restrictions beyond my control, two limitations currently exist:

1.  Google Cloud Deployment
    I could not deploy the app on Google Cloud Platform because I do not possess an international bank account or credit card, which is required to activate the Cloud Run service.

2.  OpenAI API Billing Limit
    The provided OpenAI API key has reached its usage limit, resulting in the following error during runtime:


    Image generation failed: Error code: 400 - {
    'error': {
        'message': 'Billing hard limit has been reached',
        'type': 'image_generation_user_error',
        'code': 'billing_hard_limit_reached'
    }
}


Final Notes:

Despite the above limitations, the application structure, business logic, and test coverage are all complete and reflect a production-ready architecture.
Once the billing and deployment barriers are resolved, the app can be deployed seamlessly.
=======
# text2image_service
>>>>>>> 42acaaaaca46a539555851e7256e768b4df0a512
