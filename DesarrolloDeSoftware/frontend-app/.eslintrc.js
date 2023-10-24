// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/recommended'
  ],
  plugins: [
    'vue'
  ],
  rules: {
    'no-console': 'off',
  }
}
