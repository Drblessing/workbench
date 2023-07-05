const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js', // Entry point of your app
  mode: 'development', // Set the mode to development for local development
  devServer: {
    static: './dist', // Serve the files from the dist directory
    open: true, // Open the browser after server has been started
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: 'index.html', // Use the index.html file as a template
    }),
  ],
  output: {
    filename: 'main.js', // Output bundle name
    path: path.resolve(__dirname, 'dist'), // Output directory
    clean: true, // Clean the output directory before each build
  },
};
