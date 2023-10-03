const twilio = require('twilio');

const accountSid = 'ACfbf3a2cc00f08043b9f8338c2d952600';
const authToken = '9ef238af45b106606debef26e749368a';

const twilioPhoneNumber = '+61415760314';

const client = new twilio(accountSid, authToken);

function generateOTP() {
    return Math.floor(100000 + Math.random() * 900000);
}

function sendOTP(phoneNumber, otp) {
    const message = `Your OTP is: ${otp}`;

    return client.messages
        .create({
            body: message,
            from: twilioPhoneNumber,
            to: phoneNumber
        })
        .then(message => {
            console.log(`OTP sent successfully to ${phoneNumber}. Message SID: ${message.sid}`);
            return true; 
        })
        .catch(error => {
            console.error(`Failed to send OTP to ${phoneNumber}: ${error.message}`);
            return false; 
        });
}

const otpForm = document.getElementById("otpForm");

otpForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const phoneNumberInput = document.getElementById("phoneNumber");
    const phoneNumber = phoneNumberInput.value.trim();

    if (!phoneNumber) {
        alert("Please enter a valid phone number.");
        return;
    }

    const otp = generateOTP();

    sendOTP(phoneNumber, otp)
        .then(function (success) {
            if (success) {
                alert("OTP sent successfully. Check your phone for the code.");
            
            } else {
                alert("Failed to send OTP. Please try again later.");
            }
        })
        .catch(function (error) {
            console.error(error);
            alert("An error occurred while sending OTP. Please try again later.");
        });
});
