const webpack = require("webpack");
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: [
    'babel-polyfill',
    __dirname + '/src/index.js',
  ],
  output: {
    path: __dirname + '/dist',
    filename: 'index.js',
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: __dirname + '/src/index.html',
    }),
    new webpack.SourceMapDevToolPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          'file-loader',
        ]
      },
    ],
  },
};
