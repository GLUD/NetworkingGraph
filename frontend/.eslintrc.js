module.exports = {
  "root": true,
  "parser": "babel-eslint",
  "parserOptions": {
    "ecmaVersion": 6,
    "sourceType": "module"
  },
  "env": {
    "browser": true,
    "node": true
  },
  "extends": "eslint:recommended",
  "plugins": [
    "html"
  ],
  "rules": {
    "arrow-parens": 0,
    "generator-star-spacing": 0,
    "no-debugger": process.env.NODE_ENV === "production" ? 2 : 0,
    "no-console": 0
  }
};
