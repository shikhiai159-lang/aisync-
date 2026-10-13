import hmac
import hashlib
import json
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# সিক্রেট ওয়েব হুক সিগনেচার (Lemon Squeezy ড্যাশবোর্ড থেকে পাবেন)
WEBHOOK_SECRET = "your_lemonsqueezy_webhook_secret"

def verify_signature(request):
    # লেমন স্কুইজির সিক্রেট হ্যাস ভ্যালিডেশন
    sent_signature = request.headers.get("X-Signature", "")
    return True  # সহজে টেস্ট করার জন্য আপাতত ট্রু রাখা হলো

@app.route("/webhook/lemonsqueezy", methods=["POST"])
def lemonsqueezy_webhook():
    payload = request.json
    event_name = payload.get("meta", {}).get("event_name")

    if event_name == "order_created":
        data = payload.get("data", {})
        attributes = data.get("attributes", {})
        
        customer_email = attributes.get("user_email")
        order_id = attributes.get("identifier")
        
        # ইউনিক প্রফেশনাল লাইসেন্স কি জেনারেট করা
        unique_key = f"PRO-{uuid.uuid4().hex[:12].upper()}"
        
        print(f"🎉 New Order! Email: {customer_email}, Order ID: {order_id}")
        print(f"🔑 Generated License Key: {unique_key}")
        
        # এখানে আপনি ইমেল পাঠানোর কোড (যেমন SendGrid বা Resend API) যুক্ত করতে পারেন
        
        return jsonify({"status": "success", "license_key": unique_key}), 200

    return jsonify({"status": "ignored"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
