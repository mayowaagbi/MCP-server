import js from "@eslint/js";
import globals from "globals";
import tseslint from "typescript-eslint";
import pluginReact from "eslint-plugin-react";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs,ts,mts,cts,jsx,tsx}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: {
      parser: tseslint.parser,
      parserOptions: {
        ecmaVersion: 2020,
        sourceType: "module",
        ecmaFeatures: { jsx: true },
      },
      globals: globals.browser,
    },
  },
  // React config
  {
    files: ["**/*.{jsx,tsx}"],
    plugins: { react: pluginReact },
    rules: {
      // Turn off JSX-in-scope for React 17+
      "react/react-in-jsx-scope": "off",

      // Keep helpful link warnings
      "react/jsx-no-target-blank": ["warn", { enforceDynamicLinks: "always" }],
    },
    settings: {
      react: {
        version: "detect",
      },
    },
  },
  tseslint.configs.recommended,
]);
