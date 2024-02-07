import React, {FC, ReactElement} from "react";
import {Box, Stack, Typography} from "@mui/material";
import {TaskTitleField} from "./_taskTitleField";
import {TaskDescriptionField} from "./_taskDescriptionField";



export const CreateTaskFrom: FC = (): ReactElement => {
    return (
        <Box
            display="flex"
            flexDirection="column"
            alignItems="flex-start"
            width="100%"
            px={4}
            my={6}
        >
            <Typography mb={2} component="h2" variant="h6">Create a task</Typography>
            <Stack sx={{ width: '100%' }} spacing={2}>
                <TaskTitleField disabled/>
                <TaskDescriptionField/>
            </Stack>
        </Box>
    )
};
