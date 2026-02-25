def get_response(prompt):
    api_url = "https://router.huggingface.co/models/google/flan-t5-small"
    headers = {
        "Authorization": f"Bearer {st.secrets['HF_API_KEY']}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": prompt}

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": response.text}

    return response.json()
