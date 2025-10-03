import React from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

const BRAND_BLUE = "#003A70";

export default function LoginPage() {
  return (
    <div
      className="d-flex justify-content-center align-items-center min-vh-100 vw-100"
      style={{ background: "linear-gradient(135deg, #003A70, #009639)" }}
    >
      <div
        className="card shadow p-4"
        style={{
          width: "22rem",
          borderRadius: "1rem",
          backgroundColor: "#ffffff",
        }}
      >
        <div
          className="d-flex flex-column  align-items-center"
          style={{ width: "18rem" }}
        >
          <img
            src="/supermicro-logo.png " // put your logo file in public/ folder
            alt="Supermicro Logo"
            className="img-fluid mx-auto d-block" // <- centers the image
            style={{ maxHeight: 80, width: "auto" }}
          />
        </div>

        <h3 className="text-center mb-3">Login</h3>
        <form>
          <div className="mb-3">
            <label
              htmlFor="email"
              className="form-label"
              style={{ color: BRAND_BLUE }}
            >
              Email address
            </label>
            <input
              type="email"
              className="form-control"
              id="email"
              placeholder="Enter email"
              required
            />
          </div>

          <div className="mb-3">
            <label
              htmlFor="password"
              className="form-label"
              style={{ color: BRAND_BLUE }}
            >
              Password
            </label>
            <input
              type="password"
              className="form-control"
              id="password"
              placeholder="Enter password"
              required
            />
          </div>

          <div className="mb-3 form-check">
            <input
              type="checkbox"
              className="form-check-input"
              id="rememberMe"
            />
            <label
              className="form-check-label"
              htmlFor="rememberMe"
              style={{ color: BRAND_BLUE }}
            >
              Remember me
            </label>
          </div>

          <button type="submit" className="btn btn-primary w-100">
            Login
          </button>
        </form>
        {/*
        <p className="text-center mt-3 mb-0">
          Don’t have an account?{" "}
          <a href="/signup" style={{ color: BRAND_BLUE }}>
            Sign Up
          </a>
        </p>
      */}
      </div>
    </div>
  );
}
