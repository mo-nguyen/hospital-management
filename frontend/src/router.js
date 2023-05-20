import { createWebHistory, createRouter } from "vue-router";
import BasePage from "./pages/BasePage";
import DashBoardPage from "./pages/DashBoardPage";
import LoginPage from "./pages/LoginPage";

const routes = [
    {
        path: "/",
        component: BasePage,
        children: [
            {
                path: "",
                component: DashBoardPage,
            },
            {
                path: "login",
                component: LoginPage
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;