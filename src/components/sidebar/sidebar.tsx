import React, {FC, ReactElement} from "react";
import {Avatar, Grid} from "@mui/material";
import {Profile} from "../profile/profile";
import {CreateTaskFrom} from "../createTaskForm/createTaskForm";

export const Sidebar: FC = (): ReactElement => {
    return (
        <Grid item md={4} sx={{
                height: '100vh',
                position: 'fixed',
                right: 0,
                top: 0,
                width: '100%',
                backgroundColor: 'background.paper',
                display: 'flex',
                justifyContent: 'center',
                flexDirection: 'column',
                alignItems: 'center',
            }}>
            <Profile name='ridwan'/>
            <CreateTaskFrom />
        </Grid>
    );
};
