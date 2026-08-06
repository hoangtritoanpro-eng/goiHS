// firebase-config.js
const firebaseConfig = {
  apiKey: "AIzaSyDHVUuckh7wjzyQEmgIbmGGHyAffv9153E",
  authDomain: "goihs-e3b26.firebaseapp.com",
  databaseURL: "https://goihs-e3b26-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "goihs-e3b26",
  storageBucket: "goihs-e3b26.firebasestorage.app",
  messagingSenderId: "883843714629",
  appId: "1:883843714629:web:f7aaf24ce73fbfb9241d2c",
  measurementId: "G-QYHGZEBDG0"
};

// Initialize Firebase
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

// Khởi tạo Database nếu script database được import
let database;
if (firebase.database) {
    database = firebase.database();
}
