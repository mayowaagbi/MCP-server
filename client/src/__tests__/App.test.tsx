import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import App from "../App";

describe("App", () => {
  it("renders welcome text", () => {
    render(<App />);
    expect(screen.getByText(/email/i)).toBeInTheDocument();
  });
});
