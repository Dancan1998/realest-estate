import "./App.css";
import Layout from "./hocs/layout";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import {
  Home,
  About,
  Contact,
  Listings,
  SignIn,
  SignUp,
  ListingDetail,
  NotFound,
} from "./pages";
import "./sass/main.scss";

const App = () => {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/about" element={<About />} />
          <Route exact path="/listings" element={<Listings />} />
          <Route exact path="/listing/:id" element={<ListingDetail />} />
          <Route exact path="/contact" element={<Contact />} />
          <Route exact path="/login" element={<SignIn />} />
          <Route exact path="/signup" element={<SignUp />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Layout>
    </Router>
  );
};

export default App;
